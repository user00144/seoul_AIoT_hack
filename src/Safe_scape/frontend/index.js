window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 37.5400456, lng: 126.9921017 },
        zoom: 15
    });

    const malls = [
        {
            label: "A",
            name: "벤치 A",
            lat: 37.528888,
            lng: 127.019850,
            image: "../pic/bench_A.png",
            description: "손상정도 6/10 -- 고위험군.",
            type: "벤치",
            ids: "BE202",
            date: "2024-09-18"
        },
        {
            label: "B",
            name: "골대 A",
            lat: 37.529219,
            lng: 127.021642,
            image: "../pic/court_A.png",
            description: "손상정도 4/10.",
            type: "골대",
            ids: "CO941",
            date: "2024-10-3"
        },
        {
            label: "C",
            name: "미끄럼틀 A",
            lat: 37.526326,
            lng: 127.018213,
            image: "../pic/slide_A.png",
            description: "손상정도 5/10.",
            type: "미끄럼틀",
            ids: "SL146",
            date: "2024-10-7"
        },
        {
            label: "D",
            name: "그네 A",
            lat: 37.527037,
            lng: 127.019704,
            image: "../pic/swing_A.png",
            description: "손상정도 4/10.",
            type: "그네",
            ids: "SW123",
            date: "2024-10-05"
        },
        {
            label: "D",
            name: "그네 A",
            lat: 37.527037,
            lng: 127.019704,
            image: "../pic/swing_A.png",
            description: "손상정도 4/10.",
            type: "그네",
            ids: "SW123",
            date: "2024-10-05"
        }
    ];

    let dynamicMarker;
    const bounds = new google.maps.LatLngBounds();
    const infoWindow = new google.maps.InfoWindow();

    malls.forEach(({ label, name, lat, lng, image, description, type, ids, date }) => {
        const marker = new google.maps.Marker({
            position: { lat, lng },
            label,
            map
        });
        bounds.extend(marker.position);

        marker.addListener("click", () => {
            const content = `
                <div class="card" style="width: 18rem;">
                    <img src="${image}" class="card-img-top" alt="${name}" style="height: 150px; object-fit: cover;">
                     <div class="card-body">
                     <p class="card-text">
                     <strong>일련번호 :</strong>:${ids}<br>
                        <strong>유형:</strong>${type}<br>
                            <strong>GPS :</strong>${lat}, ${lng}<br>
                            <strong>손상 정보:</strong> <span class="badge text-bg-danger">$${description}</span><br>
                            <strong>일시:</strong>${date}<br>
                        </p>
                    </div>
                </div>
            `;
            infoWindow.setContent(content);
            infoWindow.open({
                anchor: marker,
                map
            });
        });
    });

    // fitBounds로 위치 맞춤 후 적절한 줌 레벨 설정
    map.fitBounds(bounds);

    // 실시간 업데이트 함수
    async function updateDynamicMarker() {
        try {
            const response = await fetch("http://127.0.0.1:8000/get_acc");
            const {label, name, lat, lng, description} = await response.json();
            if (dynamicMarker) {
                dynamicMarker.setPosition({ lat, lng });
            } else {
                dynamicMarker = new google.maps.Marker({
                    position: { lat, lng },
                    label,
                    map
                });
            }

            dynamicMarker.addListener("click", () => {
                const content = `
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                                <strong>GPS:</strong> ${lat}, ${lng}<br>
                                <strong>손상 정보:</strong> <span class="badge text-bg-danger">${description}</span><br>
                        </div>
                    </div>
                `;
                infoWindow.setContent(content);
                infoWindow.open({
                    anchor: dynamicMarker,
                    map
                });
            });
        } catch (error) {
            console.error("Failed to fetch location data:", error);
        }
    }

    // 일정 주기로 업데이트 (예: 10초마다)
    updateDynamicMarker();
    setInterval(updateDynamicMarker, 10000); // 10초마다 업데이트
};

